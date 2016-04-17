var React = require('react');
var ReactDOM = require('react-dom');

var USER_DATA = {
  name: 'Grégoire     Fouillard',
  username: "greg28",
  image: 'https://avatars3.githubusercontent.com/u/5723730?v=3&u=4370bd538b86ad85bc589fa42cfbdd36224e217a&s=140'
};

var HelloWorld = React.createClass({
  render: function() {
    console.log(this.props)
    return (
      <div>
        Hello {this.props.name}
      </div>
    )
  }
});

var HelloUser = React.createClass({
  render: function(){
    return (
      <div> Hello, {this.props.name}</div>
    )
  }
});

var FriendsContainer = React.createClass({
  render: function(){
    var name = 'Tyler McGinnis'
    var friends = ['Ean Platter', 'Murphy Randall', 'Merrick Christensen']
    return (
      <div>
        <h3> Name: {name} </h3>
        <ShowList names={friends} />
      </div>
    )
  }
});

var ShowList = React.createClass({
  render: function(){
    var listItems = this.props.names.map(function(friend){
      return <li> {friend} </li>;
    });
    return (
      <div>
        <h3> Friends </h3>
        <ul>
          {listItems}
        </ul>
      </div>
    )
  }
});

var ProfilePic = React.createClass({
   render: function() {
     return (
       <img src={this.props.imageUrl} style={{height: 100, width:100}}/>
     )
   }
 })
 var ProfileLink = React.createClass({
   render: function() {
     return (
       <div>
        <a href={'https://github.com/' + this.props.username}>
          {this.props.username}
        </a>
       </div>
     )
   }
 })

 var ProfileName = React.createClass({
   render: function() {
     return (
       <div>
          {this.props.name}
       </div>
     )
   }
 })

 var Avatar = React.createClass({
   render: function() {
     return (
       <div>
        <ProfilePic imageUrl={this.props.user.image} />
      <ProfileName name={this.props.user.name} />
        <ProfileLink username={this.props.user.username} />
      </div>
     )
   }
 })


ReactDOM.render(<Avatar user={USER_DATA}/>, document.getElementById('app'));
