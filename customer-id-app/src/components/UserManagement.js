import React from "react";import AddUserForm from "./AddUserForm";import CheckUserForm from "./CheckUserForm";
const UserManagement = () => {  return (    <div className="user-management-container">      <h1>User Management</h1>      <div className="form-section">        <AddUserForm />        <CheckUserForm />      </div>    </div>  );};
export default UserManagement;