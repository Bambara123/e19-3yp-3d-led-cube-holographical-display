// const mongoose = require('mongoose');
// const Schema = mongoose.Schema;

// const postFileSchema = new Schema({
//   email: { type: String, required: true },
const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const postFileSchema = new Schema({
  email: { type: String, required: true },
  image: { type: Buffer },
  video: { type: Buffer },
  code: { type: Buffer },
  object: { type: Buffer },

  reactions: {
    count: { type: Number, default: 0 },
    users: [{ type: String }], // Array of user emails who liked the post
  },
  commentsCount: { type: Number, default: 0 },
  //comments: { type: [String], default: [] },
  comments: [
    {
      userName: { type: String, required: true },
      comment: { type: String, required: true },
    },
  ],
  caption: { type: String },
  createdAt: { type: String }, // Not required, set automatically using middleware
  shareCount: { type: Number, default: 0 },
  downloadCountCode: { type: Number, default: 0 },
  downloadCountObject: { type: Number, default: 0 },
});

// Set the creation date before saving the document
postFileSchema.pre("save", function (next) {
  if (!this.createdAt) {
    const currentDate = new Date();
    const options = { year: "numeric", month: "long", day: "numeric" };
    this.createdAt = currentDate.toLocaleDateString("en-US", options);
  }
  next();
});

const PostFile = mongoose.model("PostFile", postFileSchema);

module.exports = PostFile;
