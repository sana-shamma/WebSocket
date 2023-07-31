import {socket} from './connections'

export default class MyWords {
 
    async get_all_words() {
    socket.send(
      JSON.stringify({
        type: "get_words",
        value: "",
      })
    );
  }

  async delete_word(title) {
    socket.send(
      JSON.stringify({
        type: "delete_word",
        value: `${title}`,
      })
    );
  }

  async add_word(title,content ) {
    socket.send(
      JSON.stringify({
        type: "add_word",
        value: JSON.stringify({"title":title,"meaning":content }),
      })
    );
  }
}