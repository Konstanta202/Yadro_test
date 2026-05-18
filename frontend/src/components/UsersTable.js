import React, { useState } from 'react';
import './UsersTable.css';

function UsersTable({ users, onUserClick }) {
  const [currentPage, setCurrentPage] = useState(1);
  const [jumpPage, setJumpPage] = useState('');
  const usersPerPage = 20;

  const indexOfLastUser = currentPage * usersPerPage;
  const indexOfFirstUser = indexOfLastUser - usersPerPage;
  const currentUsers = users.slice(indexOfFirstUser, indexOfLastUser);
  const totalPages = Math.ceil(users.length / usersPerPage);

  const paginate = (pageNumber) => {
    if (pageNumber >= 1 && pageNumber <= totalPages) {
      setCurrentPage(pageNumber);
      setJumpPage('');
    }
  };

  const handleJumpSubmit = (e) => {
    e.preventDefault();
    const page = parseInt(jumpPage);
    if (page >= 1 && page <= totalPages) {
      paginate(page);
    }
  };

  const getPageNumbers = () => {
    const pages = [];
    const maxVisiblePages = 5;
    
    if (totalPages <= 7) {
      for (let i = 1; i <= totalPages; i++) {
        pages.push(i);
      }
    } else {
      pages.push(1);
      
      if (currentPage > 3) {
        pages.push('...');
      }
      
      for (let i = Math.max(2, currentPage - 1); i <= Math.min(totalPages - 1, currentPage + 1); i++) {
        pages.push(i);
      }
      
      if (currentPage < totalPages - 2) {
        pages.push('...');
      }
      
      if (totalPages > 1) {
        pages.push(totalPages);
      }
    }
    
    return pages;
  };

  return (
    <div className="users-table-container">
      <h2>Список пользователей ({users.length})</h2>
      
      <div className="table-responsive">
        <table className="users-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Пол</th>
              <th>Имя</th>
              <th>Фамилия</th>
              <th>Телефон</th>
              <th>Email</th>
              <th>Адрес</th>
              <th>Действия</th>
            </tr>
          </thead>
          <tbody>
            {currentUsers.map(user => (
              <tr key={user.id}>
                <td>{user.id}</td>
                <td>{user.gender === 'man' ? 'Мужской' : user.gender === 'woman' ? 'Женский' : user.gender}</td>
                <td>{user.first_name}</td>
                <td>{user.last_name}</td>
                <td>{user.phone}</td>
                <td>{user.email}</td>
                <td>{user.address}</td>
                <td>
                  <button 
                    className="btn-detail"
                    onClick={() => onUserClick(user)}
                  >
                    Подробнее
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {totalPages > 1 && (
        <div className="pagination-container">
          <div className="pagination">
            <button 
              onClick={() => paginate(currentPage - 1)}
              disabled={currentPage === 1}
              className="btn-page"
            >
              &laquo; Назад
            </button>
            
            <div className="page-numbers">
              {getPageNumbers().map((page, index) => (
                page === '...' ? (
                  <div key={`dots-${index}`} className="dots-group">
                    <span className="dots">...</span>
                    <form onSubmit={handleJumpSubmit} className="jump-form">
                      <input
                        type="number"
                        min="1"
                        max={totalPages}
                        placeholder="№"
                        value={jumpPage}
                        onChange={(e) => setJumpPage(e.target.value)}
                        className="jump-input"
                      />
                      <button type="submit" className="jump-btn">→</button>
                    </form>
                  </div>
                ) : (
                  <button
                    key={page}
                    onClick={() => paginate(page)}
                    className={`btn-page ${currentPage === page ? 'active' : ''}`}
                  >
                    {page}
                  </button>
                )
              ))}
            </div>
            
            <button 
              onClick={() => paginate(currentPage + 1)}
              disabled={currentPage === totalPages}
              className="btn-page"
            >
              Вперед &raquo;
            </button>
          </div>
          
          <div className="page-info">
            Страница {currentPage} из {totalPages}
          </div>
        </div>
      )}
    </div>
  );
}

export default UsersTable;