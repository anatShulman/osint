import React, { useEffect, useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import {
  AppBar,
  Button,
  Toolbar,
  Typography,
  makeStyles,
} from '@material-ui/core';




const AllMacines = () => {
  const [data,setData]=useState([]);

  useEffect(()=>{
    fetch("http://localhost:5000/getMachines",{
      method:"GET",
    })
    .then((res)=>res.json())
    .then((data)=>{
      console.log(data,"AllMachine");
      setData(data.data);
    });
   },[]);
  return (
    <div className="auth-wrapper">
    <div className="auth-inner" style={{width:"auto"}}>
      <Typography variant="h4" gutterBottom>
      All Machines
    </Typography>
    <table style={{width:500}}>
        <tr>
          <th>Email</th>
          <th>User</th>
          <th>MAC</th>
        </tr>
        {data.map(i=>{
          return(
            <tr>
            <td>{i.email}</td>
            <td>{i.user}</td>
            <td>{i.MAC}</td>
            </tr>
          )
        })}
        </table>
     </div>
    </div>
  );
}
export default AllMacines;
