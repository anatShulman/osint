
import React, {Component} from "react";

const EXE_URL = "https://github.com/anatShulman/osint/raw/master/exe/GUI.exe"

export default class UserDetails extends Component{
    constructor(props){
        super(props);
        this.state={
          userData:"",
        };
       
      }
    componentDidMount(){
        fetch("http://localhost:5000/userData",{
            method:"POST",
            crossDomain:true,
            headers:{
              "Content-Type": "application/json",
            Accept:"appliction/json",
            "Access-Control-Allow-Origin":"*",
            },
            body:JSON.stringify({
             token:window.localStorage.getItem("token"),
            }),
          })
          .then((res)=>res.json())
          .then((data)=>{
            console.log(data,"userData");
            this.setState({userData: data.data});

            if (data.data == "token expired") {
              alert("Token expired login again");
              window.localStorage.clear();
              window.location.href = "./sign-in";
            }
          });
        
    }
    logOut=()=>{
        window.localStorage.clear();
        window.location.href="./sign-in";
    }

    download_file=(url)=>{
        const aTag = document.createElement("a");
        aTag.href = url;
        document.body.appendChild(aTag);
        aTag.click()
        aTag.remove();
    }

    render(){
        return (
            <div>
                Name<h1>{this.state.userData.fname}</h1>
                Email<h1>{this.state.userData.email}</h1>
                <br/>
                <button onClick={()=>{this.download_file(EXE_URL)}} className="btn btn-primary"  >Download EXE</button>
                <br/>
                
                <button  onClick={this.logOut} className="btn btn-primary">Log Out</button>
            </div>
        );
    }
}