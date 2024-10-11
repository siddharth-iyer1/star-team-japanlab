''' OLD API FROM WHEN WE WERE USING SUPABASE '''

from fastapi import FastAPI, HTTPException
import supabase
import os

app = FastAPI()

# Initialize Supabase client
supabase_url = 'https://bixjwbynjtwzcogjznia.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJpeGp3YnluanR3emNvZ2p6bmlhIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyNjc3MDQwMywiZXhwIjoyMDQyMzQ2NDAzfQ.bttc6NPT8-SI2oxKHlmf576jXaTfin7kSj1emPpiHJI'
supabase_client = supabase.create_client(supabase_url, supabase_key)

@app.get("/movies/era/{era_id}")
async def get_movies_by_era(era_id: int):
    try:
        response = supabase_client.table('movie_roles').select('*').eq('Era', era_id).execute()
        movies = response.data
        if not movies:
            raise HTTPException(status_code=404, detail="Movies not found for the given era")
        return {"movies": movies}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/movies/before/{year}")
async def get_movies_before_year(year: int):
    try:
        response = supabase_client.table('movie_roles').select('*').lt('Year', year).execute()
        movies = response.data
        if not movies:
            raise HTTPException(status_code=404, detail="Movies not found before the given year")
        return {"movies": movies}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/movies/metrics/{movie_role_id}")
async def get_movie_metrics(movie_role_id: int):
    try:
        response = supabase_client.table('movie_role_metrics').select('*').eq('movieRoleId', movie_role_id).execute()
        metrics = response.data
        if not metrics:
            raise HTTPException(status_code=404, detail="Metrics not found for the given movieRoleId")
        return {"metrics": metrics}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))