
class Component extends React.Component {

    constructor (){
        super()
        this.state = {
            gym : {
                "location_name": "Default",
                "number_of_people": 12,
                "capacity": 50
            }
        }
    }

    componentWillMount(){
        var this_ = this

        $.get('http://127.0.0.1:8000/api/gym', function (data, status) {
            console.log("Retreived data: ", data)
            this_.setState({gym: data})

            plot_donut("gym-donut", data.number_of_people, data.capacity)

        })

    }

    componentDidMount(){

        var this_ = this
        var socket = new WebSocket('ws://' + window.location.host + '/streams/');
        socket.onopen = function open() {
            console.log("WebSocket connection created");
        }

        socket.onmessage = function message (event) {
            console.log("Received data...")
            var data = JSON.parse(event.data);

            this_.setState({gym: data})
            plot_donut("gym-donut", data.number_of_people, data.capacity)
        }

        if (socket.readyState == WebSocket.OPEN) {
            socket.onopen();
        }
    }

    render() {

        var imgStyle = {
            height: "400px",
            width: "100%",
        }

        var cardStyle = {
            padding:"5px",
        }

        var data = this.state.gym
        
        return ( 
            <div className="col s12 m6" style={cardStyle}>
              <div className="card">
                <div className="card-image">
                  <img src={data.image} style={imgStyle}/>
                  <span className="card-title">{data.location_name}</span>
                </div>
              </div>
            </div>
        )

    }
}

ReactDOM.render(<Component />,document.getElementById('component'))