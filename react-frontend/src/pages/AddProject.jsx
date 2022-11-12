import React from 'react';
import './form.css'
import {useState} from "react";
import { useNavigate } from 'react-router-dom';

function AddProject() {
    const [project, setProject] = useState({
        title: "",
        description: "",
    });

    const navigate = useNavigate();

    const createStudent = async (e) => {
        e.preventDefault()
        await fetch(`/api/projects/new/`,{
            method: 'POST',
            headers: {
                "Content-Type": 'application/json'
            },
            body:JSON.stringify(project)
        });
        navigate('/');
    }

    return (
        <div className='form-container'>
            <div className='form-wrap'>
                <h1 className='form-title'> Create Project </h1>
                <div className="form-box">
                    <form onSubmit={createStudent} className='form-content'>

                        <input className='form-item' type="text" name='title' placeholder='Title' onChange={e => {setProject({...project,"title": e.target.value})}} value={project.name} required/>
                        <textarea className='form-item' name="description" id="description" cols="30" rows="5" placeholder='Description' onChange={e => {setProject({...project,"description": e.target.value})}} value={project.description} required />

                        <input type="submit" formMethod='POST' formAction='/api/projects/new/' className='submit--outline submit--medium'/>

                    </form>
                </div>
            </div>
        </div>
    );
}

export default AddProject;