# Universities Information

## Getting started
If you want use this project, you must to follow this steps:

1. Clone or [fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) repository.

    ```bash
      git clone https://github.com/carandev/universities-info.git 
    ```

2. Move to repository folder.

    ```bash
    cd universities-info
    ```

3. Install frontend dependencies.
    
    ```bash
    npm install
    ```

4. Move to backend folder.

    ```bash
    cd backend
    ```

5. Create python virtual enviroment.

    ```bash
    python -m venv venv
    ```

6. Activate virtual env
    
    Linux: `source venv/bin/activate`

    Windows: `venv\\Scripts\\activate.bat` or `venv\\Scripts\\activate.ps1`

7. And finally install python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

Run project:

  - Frontend: `npm run dev`
  - Backend: *In the backend folder* `uvicorn main:app --reload`

Enjoy with my project.
