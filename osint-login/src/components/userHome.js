// import { width } from "@mui/system";
// import React, { Component, useEffect, useState } from "react";
// import GaugeChart from 'react-gauge-chart';
// const EXE_URL = "https://github.com/anatShulman/osint/raw/master/exe/GUI.exe"


// export default function UserHome({ userData }) {
//   const logOut = () => {
//     window.localStorage.clear();
//     window.location.href = "./sign-in";
//   };

//   const download_file=(url)=>{
//       const aTag = document.createElement("a");
//       aTag.href = url;
//       document.body.appendChild(aTag);
//       aTag.click()
//       aTag.remove();
//   }

  
//   return (

      
//    <div>
//         <div>
//           Name<h1>{userData.fname}</h1>
//           <br />
//           <div style={{width:'30%'}}>
//               <GaugeChart id="gauge-chart1" />
//           </div>

//           <br />
//           <button onClick={() => { download_file(EXE_URL); } } className="btn btn-primary">Download EXE</button>
//           <button onClick={logOut} className="btn btn-primary">
//             Log Out
//           </button>
//         </div>
//       </div>
//   )
//       }




import React, { useState } from 'react';
import { Layout, Menu } from 'antd';
import UserPanel from './userPanel';
import GaugeChart from 'react-gauge-chart';
import {
  AppBar,
  Button,
  Toolbar,
  Typography,
  makeStyles,
  ListItemIcon,
  List,
  Drawer,
  Divider,
  ListItem,

  ListItemText,

} from '@material-ui/core';
import {
  UserOutlined,
  NotificationOutlined,
} from '@ant-design/icons';
import UserNotification from './UserNotiification';
const EXE_URL = "https://github.com/matankic/Agent/raw/main/Agent.exe"



const { SubMenu } = Menu;
const { Header, Content, Sider } = Layout;

const useStyles = makeStyles((theme) => ({
  
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
  },
  toolbar: theme.mixins.toolbar,
}));

const UserDashboard = () => {

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
  const classes = useStyles();
  const [selectedMenuItem, setSelectedMenuItem] = useState('Dashboard');

  const handleMenuClick = (e) => {
    setSelectedMenuItem(e.key);
  };

  

  return (
    <Layout>
      <Header className="header">
        <div className="logo" />
        <AppBar position="fixed" className={classes.appBar}>
        <Toolbar>
          <Typography variant="h6" noWrap>
            User Dashboard
          </Typography>
          {/* Add a Button component to the Toolbar */}
          <Button onClick={logOut}>Log Out</Button>
          <Button onClick={() => { download_file(EXE_URL); } } >Download EXE</Button>
        </Toolbar>
      </AppBar>

      </Header>
      <Layout>
        <Sider width={200} className="site-layout-background">
          <Menu
            mode="inline"
            selectedKeys={[selectedMenuItem]}
            onClick={handleMenuClick}
            style={{ height: '100%', borderRight: 0 }}
          >
        
            <Menu.Item key="Dashboard" icon={<UserOutlined />} 
          > Dashboard
            </Menu.Item>
      
            <Menu.Item key="All Notifications" icon={<NotificationOutlined/>}>All Notifications</Menu.Item>
           
          </Menu>
        </Sider>
        <Layout style={{ padding: '0 24px 24px' }}>
          <Content
            className="site-layout-background"
            style={{
              padding: 24,
              margin: 0,
              minHeight: 280,
            }}
          >
            {selectedMenuItem === 'Dashboard' && <UserPanel/>}
            {selectedMenuItem === 'All Notifications' && <UserNotification/>}
          </Content>
        </Layout>
      </Layout>
    </Layout>
  );
};



export default UserDashboard;

// // Import the components you want to render for each menu item
// import Dashboard from './Dashboard';
// import Users from './Users';
// import Notifications from './Notifications';
// import Settings from './Settings';

// const AdminDashboard = () => {
//   const classes = useStyles();
//   const [selectedMenuItem, setSelectedMenuItem] = useState('dashboard');

//   const handleMenuClick = (menuItem) => {
//     setSelectedMenuItem(menuItem);
//   };

//   return (
//     <div className={classes.root}>
//       <AppBar position="fixed" className={classes.appBar}>
//         <Toolbar>
//           <Typography variant="h6" noWrap>
//             Admin Dashboard
//           </Typography>
//         </Toolbar>
//       </AppBar>
//       <Drawer
//         className={classes.drawer}
//         variant="permanent"
//         classes={{
//           paper: classes.drawerPaper,
//         }}
//       >
//         <div className={classes.toolbar} />
//         <Divider />
//         <List>
//           <ListItem
//             button
//             selected={selectedMenuItem === 'dashboard'}
//             onClick={() => handleMenuClick('dashboard')}
//           >
//             <ListItemIcon>
//               <DashboardIcon />
//             </ListItemIcon>
//             <ListItemText primary="Dashboard" />
//           </ListItem>
//           <ListItem
//             button
//             selected={selectedMenuItem === 'users'}
//             onClick={() => handleMenuClick('users')}
//           >
//             <ListItemIcon>
//               <PeopleIcon />
//             </ListItemIcon>
//             <ListItemText primary="Users" />
//           </ListItem>
//           <ListItem
//             button
//             selected={selectedMenuItem === 'notifications'}
//             onClick={() => handleMenuClick('notifications')}
//           >
//             <ListItemIcon>
//               <NotificationsIcon />
//             </ListItemIcon>
//             <ListItemText primary="Notifications" />
//           </ListItem>
//           <ListItem
//             button
//             selected={selectedMenuItem === 'settings'}
//             onClick={() => handleMenuClick('settings')}
//           >
//             <ListItemIcon>
//               <SettingsIcon />
//             </ListItemIcon>
//             <ListItemText primary="Settings" />
//           </ListItem>
//         </List>
//       </Drawer>
//       <main className={classes.content}>
//         <div className={classes.toolbar} />
//         {/* Conditionally render the appropriate component based on the selected menu item */}
//         {selectedMenuItem === 'dashboard' && <Dashboard />}
//         {selectedMenuItem === 'users' && <Users />}
//         {selectedMenuItem === 'notifications' && <Notifications />}
//         {selectedMenuItem === 'settings' && <Settings />}
//       </main>
//     </div>
//   );

