import React, { createContext, useState, ReactNode, FC } from 'react';

interface Message{
    text: string,
    type: 'question' | 'answer';
}

interface ChatContextProps {
    messages: Message[];
    addMessage: (text: string, type: 'question' | 'answer') => void;
}

export const ChatContext = createContext<ChatContextProps | undefined>(undefined);

export const ChatProvider: FC<{ children: ReactNode }> = ({ children }) => {
    const [messages, setMessages] = useState<Message[]>([]);

    const addMessage = (text:string, type: 'question' | 'answer')=>{
        setMessages((prev)=>[...prev, {text,type}])
    }
    return(
        <ChatContext.Provider value={{messages, addMessage}}>
            {children}
        </ChatContext.Provider>
    )
}
