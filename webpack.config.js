const path = require("path");

module.exports = {

  entry: path.resolve(__dirname, "frontend/index.js"),
  output: {
    path: path.resolve(__dirname, "src/static/js"),
    filename: "[name].bundle.js",
    publicPath: "/static/js",
  },

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: "babel-loader",
      },
    ],
  },

  optimization: {
      minimize: true,
  },
};
