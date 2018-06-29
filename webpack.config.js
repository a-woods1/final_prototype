var path = require("path");
var webpack = require('webpack');
var ManifestRevisionPlugin = require('manifest-revision-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin')

module.exports = {
	entry: {
		"home": [path.resolve(__dirname, "./app/home/js/home.jsx")],
	},
	output: {
        path: path.join(__dirname, "static"),
		publicPath: "/static/",
		filename: "[name]-[hash].js"
	},
	plugins: [
        new CleanWebpackPlugin(["static/*.js", "static/manifest.json"], {root: __dirname, verbose: true, dry: false, exclude: ["base.css"]}),
		new ManifestRevisionPlugin(path.resolve(__dirname, "./manifest.json"), {rootAssetPath: './static', ignorePaths: ['./node_modules']}),
		new webpack.NoEmitOnErrorsPlugin(),
		new UglifyJsPlugin(),
		new webpack.optimize.AggressiveMergingPlugin(),
		new webpack.HotModuleReplacementPlugin()
	],
	module: {
		rules: [
           {
				test: /\.jsx?$/,
				exclude: /(node_modules)/,
				loader: 'babel-loader',
				query: {
					presets: ['react','es2015']
				}
			}
		]
	}
};
