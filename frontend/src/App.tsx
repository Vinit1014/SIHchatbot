import './App.css'
import Chat from './components/Chat'
import { ChatProvider } from './components/ChatContext'

function App() {

  return (
    <ChatProvider>
        {/* <h1 className="text-3xl font-bold underline">
        Hello world!
        </h1> */}
        <Chat/>
      </ChatProvider>
  )
}

export default App
