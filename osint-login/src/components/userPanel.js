import React, { useEffect, useState } from 'react';
import ReviewsBar from './reviews/ReviewsBar';
import {  Typography } from '@material-ui/core';


const UserPanel = () => {
  const [filesData, setFilesData] = useState([]);
  const [networkData, setNetworkData] = useState([]);
  const [reviewScore, setReviewScore] = useState(100);

  useEffect(() => {
    const email = localStorage.getItem("email");
    const date = localStorage.getItem("date");
    fetch("http://localhost:5000/hashes", {
      method: "POST",
      crossDomain: true,
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
        "Access-Control-Allow-Origin": "*",
      },
      body: JSON.stringify({
        email: email,
        date: date,
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data, "result");
        setFilesData(data.data);
      });
  }, []);

  useEffect(() => {
    const email = localStorage.getItem("email");
    const date = localStorage.getItem("date");
    fetch("http://localhost:5000/network-connections", {
      method: "POST",
      crossDomain: true,
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
        "Access-Control-Allow-Origin": "*",
      },
      body: JSON.stringify({
        email: email,
        date: date,
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data, "result");
        setNetworkData(data.data);
      });
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      const maxScore = Math.max(...filesData.map(item => item.malicious));
      if (maxScore !== -Infinity) {
        setReviewScore(Math.round((1 - maxScore)*100));
        clearInterval(interval);
      }
    }, 1000);
  
    return () => clearInterval(interval);
  }, [filesData]);

  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
      <div>
        <Typography variant="h4" gutterBottom>
          Dashboard
        </Typography>
      </div>

      <div className='row mt-3'>
        <div className='col-md-2' style={{ width: "200px", height: "150px" }}>
          <ReviewsBar score={reviewScore} />
        </div>
      </div>

      <div style={{ margin: "2rem 0" }}>
        <Typography variant="h6">Suspicious files:</Typography>
        <table style={{ width: "100%" }}>
          <thead>
            <tr>
              <th>Instance</th>
              <th>Name</th>
              <th>Reputation</th>
              <th>Identification</th>
              <th>sha256</th>
              <th>Path</th>
            </tr>
          </thead>
          <tbody>
            {filesData.map((item, index) => (
              <tr key={index}>
                <td style={{ wordBreak: "break-word" }}>{item.instance}</td>
                <td style={{ wordBreak: "break-word" }}>{item.name}</td>
                <td style={{ wordBreak: "break-word" }}>{item.reputation}</td>
                <td style={{ wordBreak: "break-word" }}>{parseFloat(item.malicious).toFixed(2)}</td>
                <td style={{ wordBreak: "break-word" }}>{item.sha256}</td>
                <td style={{ wordBreak: "break-word" }}>{item.path}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div style={{ margin: "2rem 0" }}>
        <Typography variant="h6">Suspicious network connections:</Typography>
        <table style={{ width: "100%" }}>
          <thead>
            <tr>
              <th>Verdict</th>
              <th>URL / Connection</th>
            </tr>
          </thead>
          <tbody>
            {networkData.map((item, index) => (
              <tr key={index}>
                <td style={{ wordBreak: "break-word" }}>{item.verdict}</td>
                <td style={{ wordBreak: "break-word" }}>{item.url}</td>
              </tr>
        ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default UserPanel;



//<td><span class="break-after-40">{item.sha256}</span></td>
