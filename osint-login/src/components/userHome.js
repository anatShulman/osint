import React, { Component, useEffect, useState } from "react";
const EXE_URL = "https://github.com/anatShulman/osint/raw/master/exe/GUI.exe"


export default function UserHome({ userData }) {
  const logOut = () => {
    window.localStorage.clear();
    window.location.href = "./sign-in";
  };

  const download_file=(url)=>{
      const aTag = document.createElement("a");
      aTag.href = url;
      document.body.appendChild(aTag);
      aTag.click()
      aTag.remove();
  }
  return (
    <div className="auth-wrapper">
        <div>
          Name<h1>{userData.fname}</h1>
          Email <h1>{userData.email}</h1>
          <br />
          <button onClick={()=>{download_file(EXE_URL)}} className="btn btn-primary"  >Download EXE</button>
          <br/>
          <button onClick={logOut} className="btn btn-primary">
            Log Out
          </button>
        </div>
    </div>
  );
}


