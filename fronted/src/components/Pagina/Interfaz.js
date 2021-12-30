import Navbar from "../Navbar/Navbar";
import React, {useState} from 'react';
import { Prediction } from "./../Reporte/Reportes";
import { Content } from "../Routes/Route";


function Interfaz(props){

    const [fileName, setFileName] = useState('');
    const [fileContent, setFileContent] = useState('');
    const [fileExtension, setFileExtension] = useState('');
    const [convertJson , setConvertJson] = useState('');
    const [prediction, setPrediction] = useState(0);

    async function handleProe (event){
        event.preventDefault();
        
        setFileExtension(fileName.split(".")[1]);
        
        var query = await Content(fileContent);
        
    }

    function handlePrection(e){
        // e.preventDefault();
        setPrediction(e.target.value)
    }

    function handleP(){
        
        console.log(prediction)
    }


    return(

        <div>
            <header>
                <Navbar 
                    fileName={setFileName}
                    fileContent = {setFileContent}
                />
            </header>

            <button className="boton" type="submit" onClick={handleProe}>Ingresar</button>

            <div className="col">
                <select className="form-select-user" value={prediction} onChange={handlePrection}>
                {

                    Prediction.map(i => {
                        return (
                            <option value={i.key} key={parseInt(i.key)}>{i.value} por Id</option>
                        )
                    })
                }
                </select>
            </div>


            <button className="boton" type="submit" onClick={handleP}>Ingresar</button>

        </div>
    );
}

export default Interfaz;

