import React, { useEffect, useState } from 'react';
import { Grid, Typography } from '@material-ui/core';
import GaugeChart from 'react-gauge-chart';

const UserPanel = () => {
  const [data,setData]=useState([]);
 useEffect(()=>{
  fetch("http://localhost:5000/hashes",{
    method:"POST",
  })
  .then((res)=>res.json())
  .then((data)=>{
    console.log(data, "hashes");
    setData(data.data);
  });
 },[]);
  
  return (
    <div>
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} sm={6} md={4}>
        <GaugeChart id="gauge-chart1" style={{width:200}}/>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <Typography variant='h6'>Suspicious files:</Typography>
        <table style={{width:300}}>
        <tr>
          <th>File Name</th>
          <th>Score</th>
          <th>identification</th>
          <th>sha256</th>
        </tr>
        {data.map(i=>{
          return(
            <tr>
            <td>{i.MAC}</td>
            <td>{i.email}</td>
            <td>{i.user}</td>
            <td>{i.sha256}</td>
            </tr>
          )
        })}
       
        </table>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
        <Typography variant='h6'>Suspicious processes:</Typography>
        <table  style={{width:200}}>
        <tr>
          <th>Process Name</th>
          <th>Path</th>
          <th>score</th>
        </tr>
        {data.map(i=>{
          return(
            <tr>
            <td>{i.MAC}</td>
            <td>{i.email}</td>
            <td>{i.user}</td>
            </tr>
          )
        })}
        </table>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
        <Typography variant='h6'>Suspicious services:</Typography>
          <table  style={{width:200}}>
        <tr>
          <th>Service Name</th>
          <th>Path</th>
         
        </tr>
        {data.map(i=>{
          return(
            <tr>
            <td>{i.MAC}</td>
            <td>{i.email}</td>
            <td>{i.user}</td>
            </tr>
          )
        })}
        </table>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
        <Typography variant='h6'>Suspicious network connactions:</Typography>
        <table  style={{width:200}}>
        <tr>
          <th>Url</th>
          <th>identification</th>
        </tr>
        {data.map(i=>{
          return(
            <tr>
            <td>{i.MAC}</td>
            <td>{i.email}</td>
            <td>{i.user}</td>
            </tr>
          )
        })}
        </table>
        </Grid>
      </Grid>
    </div>
  );
};


export default UserPanel;

