import Navbar from "../Navbar/Navbar";
import React, {useState} from 'react';
import { Prediction } from "./../Reporte/Reportes";
import { Content, Reporte1 } from "../Routes/Route";
import PolynealChart from "../Chart/PolynealChart";
import './Interfaz.css'


function Interfaz(props){

    const [fileName, setFileName] = useState('');
    const [fileContent, setFileContent] = useState('');
    const [fileExtension, setFileExtension] = useState('');
    const [prediction, setPrediction] = useState(0);
    const [dataPrediction, setDataPrediction] = useState('');

    // Etiquetas
    const [label1, setLabel1] = useState('');
    const [label2, setLabel2] = useState('');
    const [label3, setLabel3] = useState('');

    // Parametrizar
    const [parametrizar, setParametrizar] = useState('');
    const [header, setHeader] = useState([]);

    // Graph
    const [polyneal, setPolyneal] = useState(null);
    const [dispers, setDispers] = useState(null);
    const [rmse, setRmse] = useState(0);
    const [r2, setR2] = useState(0);
    const [labels, setLabels] = useState(null);


    async function handlePrediction(e){
        
        e.preventDefault();
        if(prediction == 0){ //Tendencia de la infección por Covid-19 en un País.
            if(label2 != '' || label3 != ''){
               
                // console.log(`1- ${label1}, EC1: ${label2} - EC2: ${label3}`)
                // console.log(fileContent)
                // console.log(fileExtension)
                console.log("a")
                var query = await Reporte1(label1, label2, label3, fileContent, fileExtension);
                
                var result = await query.json();

                if(query.status == 200){
                    console.log(result)
                    setDispers(result.dispers);
                    setPolyneal(result.poly);
                    setR2(result.r2);
                    setRmse(result.rmse);
                    setLabels(result.label);

                }else {
                    alert('Error')
                }

                
            }else{
                alert('Debe seleccionar un Encabezado para poder Parametrizar.')
            }
        }
       
        
    }

    function getParametrizar(e){ setParametrizar(e.target.value); }

    function handleInputChange1(e){ setLabel1(e.target.value); }
    function handleInputChange2(e){ setLabel2(e.target.value); }
    function handleInputChange3(e){ setLabel3(e.target.value); }

    return(

        <div>
            <header>
                <Navbar 
                    fileName       = {setFileName}        // Nombre de Archivo.
                    fileContent    = {setFileContent}     // Contenido del Archivo.
                    fileExtension  = {setFileExtension}   // Extensión del Archivo.
                    dataPrediction = {setPrediction}      // Predicción para el Reporte.
                    dataHeader     = {setHeader}          // Cabecera del contenido.
                />
            </header>

            
            <div className="row">
                <div className="col">
                    <div className="col-md-4">
                        <label className="form-label">PARAMETRIZAR DATOS </label>
                    </div>
                    <div>
                        <input className="etiqueta1" type="text" placeholder="Pais" value={label1} onChange={handleInputChange1} /> 
                    </div>
                   
                    <div>
                        <select className="form-option-1" value={label2} onChange={handleInputChange2}>
                            <option className="form-option">Seleccione el Primer Encabezado</option>
                            {
                                
                                header.map(i=>{
                                    return(
                                        <option className="form-option" value={i.value} key={i.key}>{i.value}</option>
                                    )
                                })
                            }
                        </select>
                    </div>
                    <div>
                        <select className="form-option-1" value={label3} onChange={handleInputChange3}>
                            <option className="form-option">Seleccione el Segundo Encabezado 2</option>
                            {
                                
                                header.map(i=>{
                                    return(
                                        <option className="form-option" value={i.value} key={i.key}>{i.value}</option>
                                    )
                                })
                            }
                        </select>
                    </div>
                    <div>
                        <button className="form-boton" type="submit" onClick={handlePrediction}>Cargar Datos</button>
                    </div>
                </div>
                <div className="col">

                </div>
               
            </div>
            <div className="row">
                <PolynealChart
                    title = {'Reporte1'} 
                    poly = {polyneal} 
                    dispers = {dispers} 
                    labels = {labels}                
                />

            </div>
            



        </div>
    );
}

export default Interfaz;

