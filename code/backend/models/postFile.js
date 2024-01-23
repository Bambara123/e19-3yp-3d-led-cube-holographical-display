// models/postFile.js
/*const mongoose = require('mongoose');

const fileSchema = new mongoose.Schema({
  email: { type: String},
  //fileType: { type: String},
  fileContent: { type: Buffer, required: true },
});

const PostFile = mongoose.model('PostFile', fileSchema);

module.exports = PostFile;*/

/*const mongoose = require('mongoose');

const fileSchema = new mongoose.Schema({
  email: { type: String },
  contentType: { type: String }, // Add this line for content type
  fileContent: { type: Buffer, required: true },
});

const PostFile = mongoose.model('PostFile', fileSchema);

module.exports = PostFile;*/

const mongoose = require('mongoose');

const fileSchema = new mongoose.Schema({
  email: { type: String },
  files: [
    {
      fileType: { type: String }, // 'image', 'video', 'code', etc.
      contentType: { type: String },
      fileContent: { type: Buffer, required: true },
    }
  ]
});

const PostFile = mongoose.model('PostFile', fileSchema);

module.exports = PostFile;


