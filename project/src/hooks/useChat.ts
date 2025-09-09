import { useState, useCallback } from 'react';
import { ChatAPI } from '../utils/api';

interface Message {
  id: string;
  text: string;
  isUser: boolean;
  timestamp: Date;
  suggestions?: string[];
  intent?: string;
  confidence?: number;
}

export const useChat = () => {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      text:
        "Hello! Welcome to RGM College of Engineering and Technology's inquiry system. I'm here to help you with information about admissions, courses, fees, facilities, campus life, and more. How can I assist you today?",
      isUser: false,
      timestamp: new Date(),
      suggestions: [
        'Tell me about admissions',
        'What courses do you offer?',
        'What are the fees?',
        'Show me campus facilities',
      ],
    },
  ]);
  const [isTyping, setIsTyping] = useState(false);
  const [isConnected, setIsConnected] = useState(true);

  const sendMessage = useCallback(async (text: string) => {
    if (!text.trim()) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      text: text.trim(),
      isUser: true,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setIsTyping(true);

    try {
      const data = await ChatAPI.sendMessage(text.trim());

      const botMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: data.response,
        isUser: false,
        timestamp: new Date(),
        suggestions: data.suggestions,
        intent: data.intent,
        confidence: data.confidence,
      };

      setMessages((prev) => [...prev, botMessage]);
      setIsConnected(true);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        text:
          "I'm sorry, I'm having trouble connecting right now. Please try again in a moment.",
        isUser: false,
        timestamp: new Date(),
        suggestions: ['Try again', 'Contact support'],
      };
      setMessages((prev) => [...prev, errorMessage]);
      setIsConnected(false);
    } finally {
      setIsTyping(false);
    }
  }, []);

  const resetConversation = useCallback(async () => {
    try {
      await ChatAPI.resetConversation();
      setMessages([
        {
          id: '1',
          text:
            "Hello! Welcome to RGM College of Engineering and Technology's inquiry system. I'm here to help you with information about admissions, courses, fees, facilities, campus life, and more. How can I assist you today?",
          isUser: false,
          timestamp: new Date(),
          suggestions: [
            'Tell me about admissions',
            'What courses do you offer?',
            'What are the fees?',
            'Show me campus facilities',
          ],
        },
      ]);
    } catch (error) {
      console.error('Error resetting conversation:', error);
    }
  }, []);

  const handleSuggestionClick = useCallback(
    (suggestion: string) => {
      void sendMessage(suggestion);
    },
    [sendMessage]
  );

  return {
    messages,
    isTyping,
    isConnected,
    sendMessage,
    resetConversation,
    handleSuggestionClick,
  };
};