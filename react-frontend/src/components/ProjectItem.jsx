import {FaTrash, FaEdit} from "react-icons/fa";
import { Link } from "react-router-dom"


function ProjectItem(props) {


    return (
        <li className='list-item'>
            <h3 className='project-title'>
                {props.project.title}
            </h3>
            <Link to={`/project/${props.project.id}`}>
                <FaEdit className='item-link' />
            </Link>
            <Link>
                <FaTrash className='item-link' onClick={() => {props.onDelete(props.project.id)}}/>
            </Link>
        </li>
    );
}

export default ProjectItem;