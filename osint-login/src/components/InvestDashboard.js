
import React, { useState } from 'react';
import { Layout, Menu } from 'antd';
import {
  UserOutlined,
  LaptopOutlined,
  NotificationOutlined,
} from '@ant-design/icons';
import AllMacines from './AllMacines';

const { SubMenu } = Menu;
const { Header, Content, Sider } = Layout;

const AdminDashboard = () => {
  const [selectedMenuItem, setSelectedMenuItem] = useState('users');

  const handleMenuClick = (e) => {
    setSelectedMenuItem(e.key);
  };

  return (
    <Layout>
      <Header className="header">
        <div className="logo" />
        <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
          <Menu.Item key="1">Dashboard</Menu.Item>
          <Menu.Item key="2">Reports</Menu.Item>
          <Menu.Item key="3">Settings</Menu.Item>
        </Menu>
      </Header>
      <Layout>
        <Sider width={200} className="site-layout-background">
          <Menu
            mode="inline"
            selectedKeys={[selectedMenuItem]}
            onClick={handleMenuClick}
            style={{ height: '100%', borderRight: 0 }}
          >
            <SubMenu key="sub1" icon={<UserOutlined />} title="Users">
              <Menu.Item key="users">All Users</Menu.Item>
            </SubMenu>
            <SubMenu key="sub2" icon={<LaptopOutlined />} title="Machines">
              <Menu.Item key="machines">All Machines</Menu.Item>
            </SubMenu>
            <SubMenu
              key="sub3"
              icon={<NotificationOutlined />}
              title="Notifications"
            >
              <Menu.Item key="notifications">All Notifications</Menu.Item>
              <Menu.Item key="add-notification">Add Notification</Menu.Item>
            </SubMenu>
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
            {/* This is where you would render the appropriate component based on the selected menu item */}
            {selectedMenuItem === 'users' && <h1>All Users</h1>}
            {selectedMenuItem === 'add-user' && <h1>Add User</h1>}
            {selectedMenuItem === 'machines' && <AllMacines/>}
  
            {selectedMenuItem === 'notifications' && (
              <h1>All Notifications</h1>
            )}
            {selectedMenuItem === 'add-notification' && (
              <h1>Add Notification</h1>
            )}
          </Content>
        </Layout>
      </Layout>
    </Layout>
  );
};

export default AdminDashboard;