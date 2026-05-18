import React, { useState, useEffect, useCallback } from 'react';
import UsersTable from './components/UsersTable';
import UserDetail from './components/UserDetail';
import UserForm from './components/UserForm';
import { getUsers } from './services/api';
import './App.css';

function App() {
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchUsers = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await getUsers();
      setUsers(response.data);
    } catch (err) {
      setError('Ошибка при загрузке пользователей');
      console.error(err);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchUsers();
  }, [fetchUsers]);

  useEffect(() => {
    const handleShowUser = (event) => {
      setSelectedUser(event.detail);
    };
    
    window.addEventListener('showUser', handleShowUser);
    return () => window.removeEventListener('showUser', handleShowUser);
  }, []);

  const handleUserClick = (user) => {
    setSelectedUser(user);
  };

  const handleBack = () => {
    setSelectedUser(null);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Random People Database</h1>
      </header>
      
      <main className="App-main">
        {selectedUser ? (
          <UserDetail user={selectedUser} onBack={handleBack} />
        ) : (
          <>
            <UserForm onUsersLoaded={fetchUsers} />
            
            {loading && <div className="loading">Загрузка...</div>}
            {error && <div className="error">{error}</div>}
            
            {!loading && !error && (
              <UsersTable 
                users={users} 
                onUserClick={handleUserClick} 
              />
            )}
          </>
        )}
      </main>
    </div>
  );
}

export default App;