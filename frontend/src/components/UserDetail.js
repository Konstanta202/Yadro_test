import React from 'react';
import './UserDetail.css';

function UserDetail({ user, onBack }) {
  if (!user) return null;

  return (
    <div className="user-detail">
      <div className="user-detail-header">
        <button className="btn-back" onClick={onBack}>
          &larr; Назад к списку
        </button>
        <h2>{user.first_name} {user.last_name}</h2>
      </div>

      <div className="user-detail-content">
        <div className="detail-section">
          <h3>Основная информация</h3>
          <div className="detail-grid">
            <div className="detail-item">
              <label>ID:</label>
              <span>{user.id}</span>
            </div>
            <div className="detail-item">
              <label>Пол:</label>
              <span>{user.gender}</span>
            </div>
            <div className="detail-item">
              <label>Дата рождения:</label>
              <span>{user.date_of_birth || 'Не указана'}</span>
            </div>
            <div className="detail-item">
              <label>Телефон:</label>
              <span>{user.phone || 'Не указан'}</span>
            </div>
            <div className="detail-item">
              <label>Email:</label>
              <span>{user.email || 'Не указан'}</span>
            </div>
            <div className="detail-item">
              <label>Логин:</label>
              <span>{user.login || 'Не указан'}</span>
            </div>
          </div>
        </div>

        <div className="detail-section">
          <h3>Адрес</h3>
          <div className="detail-grid">
            <div className="detail-item">
              <label>Адрес:</label>
              <span>{user.address || 'Не указан'}</span>
            </div>
            <div className="detail-item">
              <label>Город:</label>
              <span>{user.city || 'Не указан'}</span>
            </div>
            <div className="detail-item">
              <label>Регион:</label>
              <span>{user.region || 'Не указан'}</span>
            </div>
            <div className="detail-item">
              <label>Страна:</label>
              <span>{user.country || 'Не указана'}</span>
            </div>
          </div>
        </div>

        <div className="detail-section">
          <h3>Паспортные данные</h3>
          <div className="detail-grid">
            <div className="detail-item">
              <label>Паспорт:</label>
              <span>{user.passport_num || 'Не указан'}</span>
            </div>
            <div className="detail-item">
              <label>Выдан:</label>
              <span>{user.passport_issued || 'Не указано'}</span>
            </div>
            <div className="detail-item">
              <label>Дата выдачи:</label>
              <span>{user.passport_date || 'Не указана'}</span>
            </div>
          </div>
        </div>

        <div className="detail-section">
          <h3>Документы</h3>
          <div className="detail-grid">
            <div className="detail-item">
              <label>ИНН:</label>
              <span>{user.inn_fiz || 'Не указан'}</span>
            </div>
            <div className="detail-item">
              <label>СНИЛС:</label>
              <span>{user.snils || 'Не указан'}</span>
            </div>
            <div className="detail-item">
              <label>ОМС:</label>
              <span>{user.oms || 'Не указан'}</span>
            </div>
          </div>
        </div>

        {user.bank_card && (
          <div className="detail-section">
            <h3>Банковские данные</h3>
            <div className="detail-grid">
              <div className="detail-item">
                <label>Карта:</label>
                <span>{user.bank_card}</span>
              </div>
              <div className="detail-item">
                <label>Владелец:</label>
                <span>{user.bank_client || 'Не указан'}</span>
              </div>
            </div>
          </div>
        )}

        {user.car_brand && (
          <div className="detail-section">
            <h3>Автомобиль</h3>
            <div className="detail-grid">
              <div className="detail-item">
                <label>Марка:</label>
                <span>{user.car_brand} {user.car_model || ''}</span>
              </div>
              <div className="detail-item">
                <label>Год:</label>
                <span>{user.car_year || 'Не указан'}</span>
              </div>
              <div className="detail-item">
                <label>Номер:</label>
                <span>{user.car_number || 'Не указан'}</span>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default UserDetail;