import React, { useState } from 'react';
import { getUserById, getRandomUser, loadUsers } from '../services/api';
import './UserForm.css';

function UserForm({ onUsersLoaded }) {
  const [loadCount, setLoadCount] = useState('');
  const [userId, setUserId] = useState('');
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');

  const handleLoadUsers = async () => {
    if (!loadCount || loadCount < 1) {
      setMessage('Введите количество от 1');
      return;
    }

    setLoading(true);
    setMessage('');
    try {
      const response = await loadUsers(parseInt(loadCount));
      setMessage(`Успешно загружено ${response.data.count} пользователей`);
      setLoadCount('');
      onUsersLoaded();
    } catch (error) {
      setMessage('Ошибка при загрузке пользователей');
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  const handleGetUserById = async () => {
    if (!userId || userId < 1) {
      setMessage('Введите корректный ID');
      return;
    }

    setLoading(true);
    setMessage('');
    try {
      const response = await getUserById(parseInt(userId));
      window.dispatchEvent(new CustomEvent('showUser', { detail: response.data }));
      setUserId('');
    } catch (error) {
      setMessage(`Пользователь с ID ${userId} не найден`);
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  const handleGetRandomUser = async () => {
    setLoading(true);
    setMessage('');
    try {
      const response = await getRandomUser();
      window.dispatchEvent(new CustomEvent('showUser', { detail: response.data }));
    } catch (error) {
      setMessage('Ошибка при получении случайного пользователя');
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="user-form">
      <div className="form-section">
        <h3>Загрузить пользователей из API</h3>
        <div className="form-group">
          <input
            type="number"
            placeholder="Количество"
            value={loadCount}
            onChange={(e) => setLoadCount(e.target.value)}
            min="1"
          />
          <button onClick={handleLoadUsers} disabled={loading}>
            Загрузить
          </button>
        </div>
      </div>

      <div className="form-section">
        <h3>Найти пользователя</h3>
        <div className="form-group">
          <input
            type="number"
            placeholder="ID пользователя"
            value={userId}
            onChange={(e) => setUserId(e.target.value)}
            min="1"
          />
          <button onClick={handleGetUserById} disabled={loading}>
            Найти по ID
          </button>
          <button onClick={handleGetRandomUser} disabled={loading} className="btn-random">
            Случайный
          </button>
        </div>
      </div>

      {message && (
        <div className={`message ${message.includes('Ошибка') || message.includes('не найден') ? 'error' : 'success'}`}>
          {message}
        </div>
      )}
    </div>
  );
}

export default UserForm;