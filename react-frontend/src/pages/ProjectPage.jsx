import { useParams } from 'react-router-dom'
import { useEffect, useState} from "react";
import { useNavigate } from 'react-router-dom';


function ProjectPage() {
    const {id} = useParams();
    let navigate = useNavigate();
    let [project, setProject] = useState();


    useEffect(() => {
        getProject().catch(e => console.log(e))
    }, []);

    const getProject = async () => {
        let resp = await fetch(`/api/project/${id}`),
            data = await resp.json();
        setProject(data);
    }

    const resetProject = (e) => {
        setProject({...project,description: e.target.value});
    }

    const updateProject = async () => {
        console.log(project?.description)
        await fetch(`/api/project/${id}/update/`, {
            method: 'PUT',
            headers: {
                'Content-Type' : 'application/json'
            },
            body:JSON.stringify(project)
        })
        navigate('/');
    }


    return (
        <div className='App'>
            <h1 className='title'>{project?.title}</h1>
            <textarea onKeyUp={(e) => {
                resetProject(e)
            }}
                      name="desc" cols="60" rows="17" className="description"
                      defaultValue={project?.description} />
            <button className='btn' onClick={updateProject}> Update </button>
        </div>
    );
}

export default ProjectPage;