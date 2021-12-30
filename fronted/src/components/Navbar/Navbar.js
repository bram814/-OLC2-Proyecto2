
function Navbar(props){

    function handleFileChange(e){
        var data = new FormData()
        try{
            
            const file = e.target.files[0];
            const reader = new FileReader();
            reader.readAsText(file);
            reader.onload = () => {
                props.fileName(file.name);
                props.fileContent(reader.result);
                data.append("data", e.target.files[0]);
                console.log(data)
            }
        }catch(error){
            alert(error);

        }
		
	}

    
    return(
        <>
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container-fluid">
                    <a className="navbar-brand" href="#">Navbar</a>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarColor02" aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                    </button>

                    <div className="collapse navbar-collapse" id="navbarColor02">
                    <ul className="navbar-nav me-auto">
                        <li className="nav-item">
                        <a className="nav-link active" href="#">Home
                            <span className="visually-hidden">(current)</span>
                        </a>
                        </li>
                        <li className="nav-item">
                        <a className="nav-link" href="#">Features</a>
                        </li>
                        <li className="nav-item">
                        <a className="nav-link" href="#">Pricing</a>
                        </li>
                        <li className="nav-item">
                        <a className="nav-link" href="#">About</a>
                        </li>
                        <li className="nav-item dropdown">
                        <a className="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">Dropdown</a>
                        
                        </li>
                    </ul>
                    <form className="d-flex">
                        <input 
                            className="form-control me-sm-2" 
                            type="file"
                            accept=".csv,.xlsx,.xls, .json"
                            onChange={handleFileChange} />
                    </form>
                    </div>
                </div>
            </nav>

        </>
    );
}


export default Navbar;