import TableComp from "./TableComp"
import IconLabelButtons from "./ButtonCsv"
import '../App.module.css'
import ButtonExe from "./ButtonExe";
import Typography from '@mui/material/Typography';
import { useState, useEffect } from 'react';
import axios from 'axios';




const baseURL = 'http://localhost:9090/'; 

const FullPage = () => {
    const [data, setData] = useState([]);
    useEffect(() => {
        axios.get(baseURL + 'api/mitreData').then((response) => {
            const resdata=response.data.success;
            setData(resdata);
        });
    }, []);



    return (
        <div className="FullPage">
            <ButtonExe/>
            <IconLabelButtons resdata={data}/>
            <Typography align='center' variant= 'h2' style={{color:'#0039a6'}}>Welcome</Typography>
            <TableComp resdata={data}/>
        </div>
    );

};

export default FullPage;
