import React, { useEffect, useState } from 'react';
import { Grid, Typography } from '@material-ui/core';
import GaugeChart from 'react-gauge-chart';
import { Email, Margin } from '@mui/icons-material';
import LinearProgress from '@material-ui/core/LinearProgress';

const UserPanel = () => {
  const [data,setData]=useState([]);

 useEffect(()=>{
  const email = localStorage.getItem("email")
  const date = localStorage.getItem("date")
  fetch("http://localhost:5000/hashes",{
    method:"POST",
    crossDomain: true,
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      "Access-Control-Allow-Origin": "*",
    },
    body: JSON.stringify({
      email:email,
      date:date
    }),
  })
  .then((res)=>res.json())
  .then((data)=>{
    console.log(data, "result");
    setData(data.data);
  });
 },[]);

 useEffect(()=>{
  const email = localStorage.getItem("email")
  const date = localStorage.getItem("date")
  fetch("http://localhost:5000/network-connections",{
    method:"POST",
    crossDomain: true,
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      "Access-Control-Allow-Origin": "*",
    },
    body: JSON.stringify({
      email:email,
      date:date
    }),
  })
  .then((res)=>res.json())
  .then((data)=>{
    console.log(data, "result");
    setData(data.data);
  });
 },[]);
  
 return(
<div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
  <div>
    <Typography variant="h4" gutterBottom>
      Dashboard
    </Typography>
  </div>

  <div style={{ margin: '2rem 0' }}>
    <Grid container spacing={6} justify='center'>
      <Grid item xs={12} sm={6} md={4}>
        <GaugeChart id="gauge-chart1" style={{ width: 200 }} />
      </Grid>
    </Grid>
  </div>

  <div style={{ margin: '2rem 0' }}>
    <Typography variant='h6'>Suspicious files:</Typography>
    <table style={{ width: "100%" }}>
      <thead>
        <tr>
          <th>Score</th>
          <th>Identification</th>
          <th>SHA256</th>
        </tr>
      </thead>
      <tbody>
        {data.map((item, index) => (
          <tr key={index}>
            <td style={{ wordBreak: "break-word" }}>{item.reputation}</td>
            <td style={{ wordBreak: "break-word" }}>{item.malicious}</td>
            <td style={{ wordBreak: "break-word" }}>{item.sha256}</td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>

  <div style={{ margin: '2rem 0' }}>
    <Typography variant='h6'>Suspicious network connections:</Typography>
    <table style={{ width: '100%', borderSpacing: 0, borderCollapse: 'separate' }}>
      <thead>
        <tr>
          <th style={{ padding: '8px' }}>Url Log</th>
        </tr>
      </thead>
      <tbody>
        {data.map((item, index) => (
          <tr key={index}>
            <td style={{ padding: '8px', border: '1px solid black' }}>{item.urlMal}</td>
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
