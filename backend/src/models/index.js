const User = require('./User');
const Question = require('./Question');
const UserProgress = require('./UserProgress');

// Define relationships
User.hasMany(UserProgress);
UserProgress.belongsTo(User);

Question.hasMany(UserProgress);
UserProgress.belongsTo(Question);

module.exports = {
  User,
  Question,
  UserProgress
}; 