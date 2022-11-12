import './App.css'
import Header from "./components/Header.jsx";
import ProjectList from "./pages/ProjectList.jsx";
import {Routes, Route} from "react-router-dom";
import ProjectPage from "./pages/ProjectPage";
import AddProject from "./pages/AddProject";

function App() {
    return (

        <div>
            <Header />
            <Routes>
                <Route path='/' exact element={<ProjectList />} />
                <Route path='/Project/new' exact element={<AddProject />} />
                <Route path='/Project/:id/' element={<ProjectPage />} />
            </Routes>
        </div>

    );
}

export default App;