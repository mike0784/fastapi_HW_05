import uvicorn

if __name__ == '__main__':
    uvicorn.run('templates.main:app', port=8000, reload=True)