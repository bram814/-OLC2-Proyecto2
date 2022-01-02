import React from "react";
import { Line } from "react-chartjs-2";

const PolynealChart = ({ title, poly, dispers, labels }) => {
  const data = {
    labels: labels,
    
    datasets: [
      {
        label: "# of Votes",
        data: poly,
        type: 'line',
        backgroundColor: "rgba(1, 78, 254, 0.2)",
        borderColor: "rgba(1, 78, 254 , 1)",
        borderWidth: 1,
      },
      {
        label: "# of Votes",
        data: dispers,
        type: 'scatter',
        backgroundColor: "rgba(255, 99, 132, 0.2)",
        borderColor: "rgba(255, 99, 132, 1)",
        borderWidth: 1,
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
      <Line data={data} options={options} />
    </>
  );
};

export default PolynealChart;
