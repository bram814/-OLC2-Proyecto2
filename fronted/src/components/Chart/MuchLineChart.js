import React from "react";
import { Line } from "react-chartjs-2";

const MuchLineChart = ({ title, poly, dispers, labels }) => {
  const data = {
    labels: labels,
    
    datasets: [
      {
        label: "# of Votes",
        data: poly,
        type: 'scatter',
        backgroundColor: "rgba(223, 81, 81, 1)",
        borderColor: "rgba(223, 81, 81, 0.2)",
        borderWidth: 1,
      },
      {
        label: "# of Votes",
        data: dispers,
        type: 'line',
        backgroundColor: "rgba(0, 24, 231 , 2)",
        borderColor: "rgba(0, 24, 231 , 5)",
        borderWidth: 3,
      },
    ],
  };

  const options = {
    indexAxis: "x",
    elements: {
      bar: {
        borderWidth: 2,
      },
    },
    responsive: true,
    plugins: {
      legend: {
        position: "right",
      },
      title: {
        display: true,
        text: title,
      },
    },
    maintainAspectRatio: false,
  };

  return (
    <>
      <Line data={data} options={options} height={1}/>
    </>
  );
};

export default MuchLineChart;
