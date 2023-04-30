
import React, { useState } from 'react';
import { Layout, Menu } from 'antd';
import {
  UserOutlined,
  LaptopOutlined,
  NotificationOutlined,
  BugOutlined,
} from '@ant-design/icons';
import AllMacines from './AllMacines';
import AllUsers from './AllUsers';
import SuspiciousResults from './SuspiciousResults';

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
      </Header>
      <Layout>
        <Sider width={200} className="site-layout-background">
          <Menu
            mode="inline"
            selectedKeys={[selectedMenuItem]}
            onClick={handleMenuClick}
            style={{ height: '100%', borderRight: 0 }}
          >
              <Menu.Item key="users" icon={<UserOutlined />}>All Users</Menu.Item>
              <Menu.Item key="machines" icon={<LaptopOutlined />}>Machines</Menu.Item>

              <Menu.Item key="add-notification" icon={<NotificationOutlined />}>Add Notification</Menu.Item>
              <Menu.Item key="suspicious-results" icon={<BugOutlined />}>Suspicious Results</Menu.Item>
        
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
          
            {selectedMenuItem === 'users' && <AllUsers/>}
            {selectedMenuItem === 'machines' && <AllMacines/>}
            {selectedMenuItem === 'suspicious-results' && <SuspiciousResults/>}
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