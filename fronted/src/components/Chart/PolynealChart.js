import React from "react";
import { Line } from "react-chartjs-2";

const PolynealChart = ({ title, poly, dispers, labels }) => {
  const data = {
    labels: labels,
    
    datasets: [
      {
        label: "# of Votes",
        data: poly,
        type: 'scatter',
        backgroundColor: "rgba(37, 167, 37, 1)",
        borderColor: "rgba(37, 167, 37 , 5)",
        borderWidth: 1,
      },
      {
        label: "# of Votes",
        data: dispers,
        type: 'line',
        backgroundColor: "rgba(255, 99, 132, 5)",
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
