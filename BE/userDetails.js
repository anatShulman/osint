const mongoose = require("mongoose");

const UserDetailsScehma = new mongoose.Schema(
  {
    fname: String,
    lname: String,
    uname: String,
    email:  {type:String,unique:true},
    password: String,
    userType: String,
  },
  {
    collection: "UserInfo",
  }
);
const InvesDetailsScehma = new mongoose.Schema(
  {
    fname: String,
    lname: String,
    uname: String,
    email:  {type:String,unique:true},
    password: String,
    userType: String,
  },
  {
    collection: "InvesInfo",
  }
);

const CSVSchema=new mongoose.Schema(
  {
    // "instance of":String,

       sha256:String,

    //   tlsh:String,

    //   "file path":String,

    //   "file name":String,

    //   "file type":String,

      email:String,

      MAC:String,

      user:String,

      // "time scanned":String,

      // "scanned time":Date,

      // "file size":String,

      // "file extension":String,

      // "creation time":String,

      // "access time":String,

      // "modified time":String,

      // "read only":Boolean,

      // readable:Boolean,

      // writable:Boolean,

      // executable:Boolean,

      // hidden:Boolean,

      // ssdeep:Boolean,

},
{
  collection: "CSV",
}
);



mongoose.model("UserInfo", UserDetailsScehma);

mongoose.model("InvesInfo", InvesDetailsScehma);

mongoose.model("CSV",CSVSchema);
