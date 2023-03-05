import React, {useState, useEffect} from 'react';
import { Table, TableHead,TableCell,Paper,TableRow,TableContainer,TableBody} from "@mui/material";
import './Search.css'
import TablePagination from '@mui/material/TablePagination';


const TableComp = ({resdata}) => {
  const [match, setMatch] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    if(resdata.length){
      setMatch(resdata);
    }
}, [resdata]);


useEffect(() => {
  const res = resdata.filter((item) => item.name.toLowerCase().includes(searchTerm.toLowerCase()) || 
  item.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
  item.path.toLowerCase().includes(searchTerm.toLowerCase()) || 
  item.hash.toLowerCase().includes(searchTerm.toLowerCase())
  );
  
  setMatch(res);
}, [searchTerm, resdata])
  
  
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(5);

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };


  const emptyRows =
    page > 0 ? Math.max(0, (1 + page) * rowsPerPage - match.length) : 0;

  return (
    <div>
      <input
        type="text"
        style={{marginLeft:"2%", marginTop:"1%", marginBottom:"2%"}}
        id="header-search"
        placeholder="Search files"
        name="s" 
        value={searchTerm}
        onChange={(event)=>setSearchTerm(event.target.value)}/>
      <TableContainer component={Paper} style={{overflow:'auto', height:'550px'}}>
      <Table sx={{ minWidth: 600 }} size="small"  stickyHeader aria-label="sticky table"  >
        <TableHead >
          <TableRow>
            <TableCell align="center" style={{fontWeight:'bold'}} >Name </TableCell>
            <TableCell align="center" style={{fontWeight:'bold'}} >Path</TableCell>
            <TableCell align="center" style={{fontWeight:'bold'}}>Description</TableCell>
            <TableCell align="center" style={{fontWeight:'bold'}}>Hash</TableCell>
          
          </TableRow>
        </TableHead>
        <TableBody>
          {match.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage).map((item,index) => (
            <TableRow
              key={index}
              sx={{ border: 0.5 }}
            >           
              <TableCell align="center" style={{width: '5%'}}>{item.name}</TableCell>
              <TableCell align="left" style={{width: '10%'}}>{item.path}</TableCell>
              <TableCell align="cenetr" style={{width: '5%'}}>{item.description}</TableCell>
              <TableCell align="cenetr" style={{width: '5%'}}>{item.hash}</TableCell>
      
            </TableRow>
          ))}
          {emptyRows > 0 && (
                  <TableCell colSpan={6} />
              )} 
           
        </TableBody>
      </Table>
    </TableContainer>
    <TablePagination
          rowsPerPageOptions={[5, 10, 25]}
          component="div"
          count={match.length}
          rowsPerPage={rowsPerPage}
          page={page}
          onPageChange={handleChangePage}
          onRowsPerPageChange={handleChangeRowsPerPage}
    />
   </div>
  );
}
export default TableComp;

