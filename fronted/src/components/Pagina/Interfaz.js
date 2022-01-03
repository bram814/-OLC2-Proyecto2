import Navbar from "../Navbar/Navbar";
import React, {useState} from 'react';
import { Prediction } from "./../Reporte/Reportes";
import { Content, Reporte1, Reporte2} from "../Routes/Route";
import PolynealChart from "../Chart/PolynealChart";
import html2canvas from "html2canvas";
import { jsPDF } from "jspdf";
import './Interfaz.css'


function Interfaz(props){

    const [fileName, setFileName] = useState('');
    const [fileContent, setFileContent] = useState('');
    const [fileExtension, setFileExtension] = useState('');
    const [prediction, setPrediction] = useState('');
    // const [dataPrediction, setDataPrediction] = useState('');

    // Etiquetas
    const [label1, setLabel1] = useState('');
    const [label2, setLabel2] = useState('');
    const [label3, setLabel3] = useState('');
    const [label4, setLabel4] = useState(1);
    const [label5, setLabel5] = useState('');
    const [label6, setLabel6] = useState('');
    const [label7, setLabel7] = useState('');
    const [label8, setLabel8] = useState('');


    // Parametrizar
    const [parametrizar, setParametrizar] = useState('');
    const [header, setHeader] = useState([]);

    // Graph
    const [polyneal, setPolyneal] = useState(null);
    const [dispers, setDispers] = useState(null);
    const [rmse, setRmse] = useState(0);
    const [r2, setR2] = useState(0);
    const [labels, setLabels] = useState(null);
    const [predict, setPredict] = useState('')


    async function handlePrediction(e){
        
        // e.preventDefault();
        
        if(prediction == 1){ //Tendencia de la infección por Covid-19 en un País.
            console.log(prediction)
            if(label2 != '' || label3 != ''){
               
                if(label4>=1){
                    if(label1 != '' && label6 != ''){
                        var query = await Reporte1(label1, label2, label3, fileContent, fileExtension, label4, label6, label5);
                        
                        var result = await query.json();

                        if(query.status == 200){

                            setDispers(result.dispers);
                            setPolyneal(result.poly);
                            setR2(result.r2);
                            setRmse(result.rmse);
                            setLabels(result.label);

                        }else {
                            alert('Error')
                        }
                    }else if(label1 == '' && label6 ==''){
                        var query = await Reporte1(label1, label2, label3, fileContent, fileExtension, label4, label6, label5);
                        
                        var result = await query.json();

                        if(query.status == 200){

                            setDispers(result.dispers);
                            setPolyneal(result.poly);
                            setR2(result.r2);
                            setRmse(result.rmse);
                            setLabels(result.label);

                        }else {
                            alert('Error')
                        }
                    }else {
                        alert('Debe de Ingresar el Filtro')
                    }
                    
                }else{
                    alert('Grado debe de ser igual o mayor a 1.')
                }
                

                
            }else{
                alert('Debe seleccionar un Encabezado para poder Parametrizar.')
            }
        }else if(prediction == 2){ // Predicción de Infectados en un País.
            console.log(prediction)
            if(label2 != '' || label3 != ''){
               
                if(label4>=1){
                    if(label1 != '' && label6 != ''){
                        var query = await Reporte2(label1, label2, label3, fileContent, fileExtension, label4, label6, label5, label7, label8);
                        
                        var result = await query.json();

                        if(query.status == 200){

                            setDispers(result.dispers);
                            setPolyneal(result.poly);
                            setR2(result.r2);
                            setRmse(result.rmse);
                            setLabels(result.label);
                            setPredict(result.r2);

                        }else {
                            alert('Error')
                        }
                    }else if(label1 == '' && label6 ==''){
                        var query = await Reporte2(label1, label2, label3, fileContent, fileExtension, label4, label6, label5, label7, label8);
                        
                        var result = await query.json();

                        if(query.status == 200){

                            setDispers(result.dispers);
                            setPolyneal(result.poly);
                            setR2(result.r2);
                            setRmse(result.rmse);
                            setLabels(result.label);
                            setPredict(result.r2);

                        }else {
                            alert('Error')
                        }
                    }else {
                        alert('Debe de Ingresar el Filtro')
                    }
                    
                }else{
                    alert('Grado debe de ser igual o mayor a 1.')
                }
                

                
            }else{
                alert('Debe seleccionar un Encabezado para poder Parametrizar.')
            }
        }
       
        
    }

    async function handleDownload(e){
        const input = document.getElementById('DivToPrintChart');
        html2canvas(input)
        .then((canvas) => {
            let imgWidth = 200;
            let imgHeight = canvas.height * imgWidth / canvas.width;
            const imgData = canvas.toDataURL('img/png');
            const pdf = new jsPDF('p', 'mm', 'a4');
            pdf.addImage(imgData, 'PNG', 0, 0, imgWidth, imgHeight);

            pdf.save(`ReporteChart.pdf`);
        })
        ;
    }
    

    function getParametrizar(e){ setParametrizar(e.target.value); }

    function handleInputChange1(e){ setLabel1(e.target.value); }
    function handleInputChange2(e){ setLabel2(e.target.value); }
    function handleInputChange3(e){ setLabel3(e.target.value); }
    function handleInputChange4(e){ setLabel4(e.target.value); }
    function handleInputChange5(e){ setLabel5(e.target.value); }
    function handleInputChange6(e){ setLabel6(e.target.value); }
    function handleInputChange7(e){ setLabel7(e.target.value); }
    function handleInputChange8(e){ setLabel8(e.target.value); }

    return(
        <div>
             <Navbar 
                    fileName       = {setFileName}        // Nombre de Archivo.
                    fileContent    = {setFileContent}     // Contenido del Archivo.
                    fileExtension  = {setFileExtension}   // Extensión del Archivo.
                    dataPrediction = {setPrediction}      // Predicción para el Reporte.
                    dataHeader     = {setHeader}          // Cabecera del contenido.
                />
            
        <div className="container">
           
               

            
            <div className="row">
                <div className="col">
                    <div className="col-md-4">
                        <label className="form-label">PARAMETRIZAR DATOS </label>
                    </div>
                    <div>
                        <input className="etiqueta1" type="text" placeholder="Filtro" value={label1} onChange={handleInputChange1} /> 
                    </div>
                    <div>
                        <input className="etiqueta1" type="text" placeholder="Grado" value={label4} onChange={handleInputChange4} /> 
                    </div>
                    <div>
                        <select className="form-option-1" value={label6} onChange={handleInputChange6}>
                            <option className="form-option">Encabezado del Filtro</option>
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
                        <select className="form-option-1" value={label2} onChange={handleInputChange2}>
                            <option className="form-option">Seleccione el 1° Encabezado</option>
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
                            <option className="form-option">Seleccione el 2° Encabezado</option>
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
                        <select className="form-option-1" value={label5} onChange={handleInputChange5}>
                            <option className="form-option">Encabezado Tiempo</option> 
                            <option className="form-option" value={1} key={1}>Si</option>
                            <option className="form-option" value={0} key={0}>No</option>
                                 
                        </select>
                    </div>
                    <div>
                        <button className="form-boton" type="submit" onClick={handlePrediction}>Cargar Datos</button>
                    </div>
                </div>
                <div className="form-div-2">
                        
                    <label className="form-label-2">Predicción</label>
                    <input className="etiqueta7" type="text" placeholder="Prediccion" value={label7} onChange={handleInputChange7} /> 
                    <select className="form-option-3" value={label8} onChange={handleInputChange8}>
                            <option className="form-option">Encabezado Tiempo</option> 
                            <option className="form-option" value={1} key={1}>Si</option>
                            <option className="form-option" value={0} key={0}>No</option>
                                 
                    </select>
                </div>
            
            </div>
            </div>
            <div className="container">

            
                <div id="DivToPrintChart">
                    <div>
                        <center>
                            <h6 className="form-predict">{rmse}</h6>
                            <h6 className="form-predict">Predicción {predict}</h6>
                        </center>
                    </div>
                    <div>
                            
                        <PolynealChart
                            title = {rmse} 
                            poly = {polyneal} 
                            dispers = {dispers} 
                            labels = {labels}                
                        />

                    </div>
                </div>
             
              
                <button className="form-boton" type="submit" onClick={handleDownload}>Descargar</button>
                </div>

        </div>
    );
}

export default Interfaz;

