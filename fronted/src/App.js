import React from "react";
import Interfaz from "./components/Pagina/Interfaz";
import "./styles.css";

// import { Line } from "react-chartjs-2";
import BarChart from "./components/BarChart";

// const data = {
//   labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
//   datasets: [
//     {
//       label: "First dataset",
//       data: [33, 53, 85, 41, 44, 65],
//       fill: true,
//       backgroundColor: "rgba(75,192,192,0.2)",
//       borderColor: "rgba(75,192,192,1)"
//     },
//     {
//       label: "Second dataset",
//       data: [33, 25, 35, 51, 54, 76],
//       fill: false,
//       borderColor: "#742774"
//     }
//   ]
// };

export default function App() {
  return (
    <div>
      <Interfaz />
    </div>
    // <div className="App">
    //   <BarChart 
    //     value={[12, 19, 3, 5, 2, 3]} 
    //     labels={['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']}
    //     title={"hola"}
    //   />
    // </div>
  );
}
