import React from "react";
import { faSpotify } from "@fortawesome/free-brands-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { BACKEND_URL } from "../consts";

class Authentication extends React.Component {
  handleClick = () => {
    window.location.href = BACKEND_URL + "/authenticate";
  };
  render = () => {
    return (
      <div className="uk-flex uk-flex-center">
        <button
          className="uk-button uk-button-default"
          onClick={this.handleClick}
        >
          Authenticate <FontAwesomeIcon icon={faSpotify} />
        </button>
      </div>
    );
  };
}

export default Authentication;
