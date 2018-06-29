var React = require("react");
var ReactDOM = require("react-dom");
var createReactClass = require("create-react-class");
 
var Home = createReactClass({
	render: function() {
		return (<div>Hi</div>);
	}
});
 
ReactDOM.render(<Home />, document.getElementById("app"));