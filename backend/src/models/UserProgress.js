const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

const UserProgress = sequelize.define('UserProgress', {
  id: {
    type: DataTypes.UUID,
    defaultValue: DataTypes.UUIDV4,
    primaryKey: true
  },
  userId: {
    type: DataTypes.UUID,
    allowNull: false,
    references: {
      model: 'Users',
      key: 'id'
    }
  },
  questionId: {
    type: DataTypes.UUID,
    allowNull: false,
    references: {
      model: 'Questions',
      key: 'id'
    }
  },
  status: {
    type: DataTypes.ENUM('attempted', 'solved', 'bookmarked'),
    allowNull: false
  },
  timeSpent: {
    type: DataTypes.INTEGER,  // in seconds
    defaultValue: 0
  },
  attempts: {
    type: DataTypes.INTEGER,
    defaultValue: 1
  },
  lastAttemptDate: {
    type: DataTypes.DATE,
    defaultValue: DataTypes.NOW
  },
  notes: {
    type: DataTypes.TEXT,
    allowNull: true
  }
});

module.exports = UserProgress; 