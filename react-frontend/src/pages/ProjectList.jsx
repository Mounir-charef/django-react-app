import{useState, useEffect} from 'react';
import ProjectItem from "../components/ProjectItem.jsx";
import {Link} from "react-router-dom";
import {FaPlus} from "react-icons/fa";

function ProjectList() {

    let [projects, setProjects] = useState([])
    useEffect(()=> {
        getProjects()
    },[])

    const getProjects = async () => {
        let resp = await fetch('/api/projects/')
        let data = await resp.json()
        setProjects(data)
    }

    const deleteProject = async (id) => {
        await fetch(`/api/project/${id}/delete`,{
            method: 'DELETE',
            headers: {
                "Content-Type": 'application/json'
            }
        })
        getProjects()
    }

    return (
        <div className='App'>
            <div className="project-list-wrap">
                <ul className='project-list'>
                    { projects.map(project => <ProjectItem key={project.id} project={project} onDelete={deleteProject}/>) }
                </ul>

                <Link to='/project/new'>
                    <button className="btn"> Add <FaPlus /> </button>
                </Link>
            </div>
        </div>
    );
}

export default ProjectList;