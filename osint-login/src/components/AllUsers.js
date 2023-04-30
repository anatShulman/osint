import React, { useEffect, useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import {
  AppBar,
  Button,
  Toolbar,
  Typography,
  makeStyles,
} from '@material-ui/core';



const AllUsers = () => {
  const [data,setData]=useState([]);

  useEffect(()=>{
    fetch("http://localhost:5000/getAllUser",{
      method:"GET",
    })
    .then((res)=>res.json())
    .then((data)=>{
      console.log(data, "userData");
      setData(data.data);
    });
   },[]);
  return (
    <div className="auth-wrapper">
    <div className="auth-inner" style={{width:"auto"}}>
      <Typography variant="h4" gutterBottom>
      All Users
    </Typography>
    <table style={{width:500}}>
        <tr>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Email</th>
        </tr>
        {data.map(i=>{
          return(
            <tr>
            <td>{i.fname}</td>
            <td>{i.lname}</td>
            <td>{i.email}</td>
            </tr>
          )
        })}
        </table>
    </div>
    </div>
  );
}
export default AllUsers;
