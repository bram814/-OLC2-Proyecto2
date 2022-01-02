import { Prediction } from "../Reporte/Reportes";
import { Content } from "../Routes/Route";
import React, {useState} from 'react';
import './Navbar.css'

function Navbar(props){


    const [prediction, setPrediction] = useState(0);
    const [fileName, setFileName] = useState('');
    const [fileExtension, setFileExtension] = useState('');
    const [fileContent, setFileContent] = useState('');

    function handleFileChange(e){
        try{
            const file = e.target.files[0];
            const reader = new FileReader();
            reader.readAsText(file);
            reader.onload = () => {
                props.fileName(file.name);
                props.fileContent(reader.result);
                props.fileExtension(file.name.split(".")[1]);
                setFileName(file.name);
                setFileContent(reader.result);
                setFileExtension(file.name.split(".")[1]);
            }
        }catch(error){
            alert(error);

        }
		
	}

    async function handleChargeFile(e){
        e.preventDefault();
        console.log("/")
        setFileExtension(fileName.split(".")[1]);
        
        var query = await Content(fileContent);
        var result = await query.json();
        
        if(query.status == 200){ // Correct
            
            props.fileName(fileName);
            props.fileExtension(fileExtension);
            props.fileContent(result.content);
            var dicHeader = [];
            var key = 0;
            result.header.map(i=>{
                
                dicHeader.push({
                    key: key,
                    value: i
                
                })

                key ++;
            })

            props.dataHeader(dicHeader)

        }else{
            alert('Error de Consulta')
        }
    }

    function handlePrection(e){
        props.dataPrediction(e.target.value)
    }
    
    return(
        <>
            <nav className="navbar navbar-expand-lg navbar-light bg-company-red">
                <div className="container-fluid">
                    <a className="navbar-brand" href="#">[OLC2]Proyecto</a>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarColor02" aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                    </button>
                    <button className="btn btn-outline-secondary me-sm-2" type="submit"  onClick={handleChargeFile} >Cargar Archivo</button>
                    <div className="collapse navbar-collapse" id="navbarColor02">
                   
                    <form className="d-flex">
                        <input className="form-control me-sm-2"  type="file" accept=".csv,.xlsx,.xls, .json" onChange={handleFileChange} />
                    </form>
                    </div>
                </div>
            </nav>
            <div className="select-div">
                <center>
                
                    <h3>Predicción: </h3>
                    <select className="form-select-user" value={prediction} onChange={handlePrection}>
                            {

                                Prediction.map(i => {
                                    return (
                                        <option value={i.key} key={parseInt(i.key)}>{i.value} por Id</option>
                                    )
                                })
                            }
                        </select>
            
                    </center>  
            </div>

        </>
    );
}


export default Navbar;

