import React, { useState, useRef, useEffect } from 'react';
import logoUrl from '../rgm-logo.png';
import { Send, MessageCircle, RefreshCw, User, Bot, Sparkles, GraduationCap, Phone, Mail, MapPin, Clock, Sun, Moon, BookOpen } from 'lucide-react';

interface Message {
  id: string;
  text: string;
  isUser: boolean;
  timestamp: Date;
  suggestions?: string[];
  intent?: string;
  confidence?: number;
}

interface ChatResponse {
  response: string;
  intent: string;
  confidence: number;
  suggestions: string[];
  timestamp: string;
}

function App() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      text: "Hello! Welcome to RGM College of Engineering and Technology's inquiry system. I'm here to help you with information about admissions, courses, fees, facilities, campus life, and more. How can I assist you today?",
      isUser: false,
      timestamp: new Date(),
      suggestions: [
        "Tell me about admissions",
        "What courses do you offer?",
        "What are the fees?",
        "Show me campus facilities"
      ]
    }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [isConnected, setIsConnected] = useState(true);
  const [isDark, setIsDark] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const handleSuggestionClick = (suggestion: string) => {
    sendMessage(suggestion);
  };

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    const stored = localStorage.getItem('theme');
    const useDark = stored ? stored === 'dark' : false;
    setIsDark(useDark);
    if (useDark) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, []);

  const toggleTheme = () => {
    const next = !isDark;
    setIsDark(next);
    if (next) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    }
  };

  const sendMessage = async (text: string) => {
    if (!text.trim()) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      text: text.trim(),
      isUser: true,
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsTyping(true);

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: text.trim() }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data: ChatResponse = await response.json();

      const botMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: data.response,
        isUser: false,
        timestamp: new Date(),
        suggestions: data.suggestions,
        intent: data.intent,
        confidence: data.confidence
      };

      setMessages(prev => [...prev, botMessage]);
      setIsConnected(true);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: "I'm sorry, I'm having trouble connecting right now. Please try again in a moment.",
        isUser: false,
        timestamp: new Date(),
        suggestions: ["Try again", "Contact support"]
      };
      setMessages(prev => [...prev, errorMessage]);
      setIsConnected(false);
    } finally {
      setIsTyping(false);
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    sendMessage(inputValue);
  };

  const handleQuickInfoClick = (info: string) => {
    sendMessage(info);
  };

  const resetConversation = async () => {
    try {
      await fetch('/api/reset', { method: 'POST' });
      setMessages([
        {
          id: '1',
          text: "Hello! Welcome to RGM College of Engineering and Technology's inquiry system. I'm here to help you with information about admissions, courses, fees, facilities, campus life, and more. How can I assist you today?",
          isUser: false,
          timestamp: new Date(),
          suggestions: [
            "Tell me about admissions",
            "What courses do you offer?",
            "What are the fees?",
            "Show me campus facilities"
          ]
        }
      ]);
    } catch (error) {
      console.error('Error resetting conversation:', error);
    }
  };

  return (
    <div className="flex flex-col h-screen transition-colors duration-500">
      <header className="flex items-center justify-between p-4 shadow-md bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm">
        <div className="flex items-center space-x-3">
          <div className="bg-gradient-to-br from-brand to-brandDark p-1 rounded-xl">
            <img src={logoUrl} alt="RGM Logo" className="h-10 w-10 object-contain bg-white rounded" />
          </div>
          <div>
            <h1 className="text-xl font-bold text-gray-900 dark:text-gray-100">RGM College of Engineering and Technology</h1>
            <p className="text-sm text-gray-600 dark:text-gray-300">College Inquiry Assistant</p>
          </div>
        </div>
        <div className="flex items-center space-x-2">
          <div className={`w-3 h-3 rounded-full ${isConnected ? 'bg-green-400' : 'bg-red-400'}`}></div>
          <span className="text-sm text-gray-600 dark:text-gray-300">
            {isConnected ? 'Connected' : 'Disconnected'}
          </span>
          <button
            onClick={toggleTheme}
            className="ml-2 p-2 text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-colors"
            title={isDark ? 'Switch to light mode' : 'Switch to dark mode'}
          >
            {isDark ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
          </button>
          <button
            onClick={resetConversation}
            className="ml-2 p-2 text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-colors"
            title="Reset conversation"
          >
            <RefreshCw className="h-4 w-4" />
          </button>
        </div>
      </header>

      <nav className="flex justify-center p-2 bg-white/60 dark:bg-gray-800/60 backdrop-blur-sm shadow-sm">
        <div className="flex space-x-2 md:space-x-4">
          <button onClick={() => sendMessage("Tell me about admissions")} className="flex items-center space-x-2 px-3 py-2 text-sm font-medium rounded-md text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
            <GraduationCap className="w-5 h-5" />
            <span className="hidden md:inline">Admissions</span>
          </button>
          <button onClick={() => sendMessage("What courses do you offer?")} className="flex items-center space-x-2 px-3 py-2 text-sm font-medium rounded-md text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
            <BookOpen className="w-5 h-5" />
            <span className="hidden md:inline">Courses</span>
          </button>
          <button onClick={() => sendMessage("How can I contact you?")} className="flex items-center space-x-2 px-3 py-2 text-sm font-medium rounded-md text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
            <Phone className="w-5 h-5" />
            <span className="hidden md:inline">Support</span>
          </button>
          <button onClick={() => inputRef.current?.focus()} className="flex items-center space-x-2 px-3 py-2 text-sm font-medium rounded-md text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
            <MessageCircle className="w-5 h-5" />
            <span className="hidden md:inline">Chat</span>
          </button>
        </div>
      </nav>

      <main className="flex-1 overflow-y-auto p-4 md:p-6">
        <div className="max-w-4xl mx-auto space-y-8">
          {messages.length <= 1 && (
            <div className="flex flex-col items-center justify-center pt-16 text-center">
              <img src={logoUrl} alt="RGM College Logo" className="h-24 w-24 opacity-50" />
              <p className="mt-4 text-lg font-medium text-gray-600 dark:text-gray-400">Start a conversation</p>
              <p className="text-sm text-gray-500 dark:text-gray-500">Ask me anything about the college!</p>
            </div>
          )}
          {messages.map((msg, index) => (
            <div key={msg.id} className={`flex items-end gap-2 ${msg.isUser ? 'justify-end' : ''}`}>
              {!msg.isUser && (
                <div className="flex-shrink-0">
                  <div className="p-2 rounded-full bg-gray-600">
                    <Bot className="h-4 w-4 text-white" />
                  </div>
                </div>
              )}
              <div className={`p-3 rounded-2xl ${msg.isUser ? 'bg-brand text-white rounded-br-md' : 'bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-gray-100 rounded-bl-md border border-gray-200 dark:border-gray-700'}`}>
                <p className="text-sm leading-relaxed">{msg.text}</p>
                {msg.confidence && !msg.isUser && (
                  <div className="mt-2 pt-2 border-t border-gray-200 dark:border-gray-700">
                    <p className="text-xs text-gray-600 dark:text-gray-400">
                      Intent: {msg.intent} ({Math.round(msg.confidence * 100)}% confidence)
                    </p>
                  </div>
                )}
              </div>
            </div>
          ))}
          
          {/* Typing Indicator */}
          {isTyping && (
            <div className="flex justify-start">
              <div className="flex items-start space-x-3 max-w-xs lg:max-w-md">
                <div className="p-2 rounded-full bg-gray-600">
                  <Bot className="h-4 w-4 text-white" />
                </div>
                <div className="p-3 bg-gray-100 dark:bg-gray-800 rounded-2xl rounded-bl-md border border-gray-200 dark:border-gray-700">
                  <div className="flex space-x-1">
                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
                  </div>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* Input Area */}
        <div className="p-4 border-t border-gray-200 dark:border-gray-800 bg-gray-50/50 dark:bg-gray-900/50">
          <form onSubmit={handleSubmit} className="flex space-x-4">
            <div className="flex-1 relative">
              <input
                ref={inputRef}
                type="text"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                placeholder="Ask about admissions, courses, fees, facilities..."
                className="w-full px-4 py-3 pr-12 border border-gray-300 dark:border-gray-700 rounded-xl focus:ring-2 focus:ring-brand focus:border-transparent outline-none transition-all duration-200 bg-white dark:bg-gray-800 dark:text-gray-100"
                disabled={isTyping}
              />
              <div className="absolute right-3 top-1/2 transform -translate-y-1/2">
                <MessageCircle className="h-5 w-5 text-gray-400" />
              </div>
            </div>
            <button
              type="submit"
              disabled={!inputValue.trim() || isTyping}
              className="px-6 py-3 bg-gradient-to-r from-brand to-brandDark text-white rounded-xl hover:opacity-95 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 transform hover:scale-105 focus:ring-2 focus:ring-brand focus:ring-offset-2 outline-none"
            >
              <Send className="h-5 w-5" />
            </button>
          </form>
          <p className="text-xs text-gray-500 mt-2 text-center">
            Ask me anything about RGM College of Engineering and Technology - I'm here to help! ✨
          </p>
        </div>
      </main>

      {/* Features Grid */}
      <div className="mt-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              <div onClick={() => handleQuickInfoClick("Tell me about admissions")} className="bg-white/70 dark:bg-gray-900/70 backdrop-blur-sm p-6 rounded-xl border border-gray-200 dark:border-gray-800 hover:shadow-lg transition-shadow duration-200 cursor-pointer">
                <div className="bg-gradient-to-br from-orange-100 to-orange-200 p-3 rounded-lg w-fit mb-4">
                  <GraduationCap className="h-6 w-6 text-brand" />
                </div>
                <h3 className="font-semibold text-gray-900 mb-2">Admissions</h3>
                <p className="text-sm text-gray-600">Requirements & Process</p>
              </div>
              <div onClick={() => handleQuickInfoClick("What courses do you offer?")} className="bg-white/70 dark:bg-gray-900/70 backdrop-blur-sm p-6 rounded-xl border border-gray-200 dark:border-gray-800 hover:shadow-lg transition-shadow duration-200 cursor-pointer">
                <div className="bg-gradient-to-br from-orange-100 to-orange-200 p-3 rounded-lg w-fit mb-4">
                  <Sparkles className="h-6 w-6 text-brand" />
                </div>
                <h3 className="font-semibold text-gray-900 mb-2">Courses</h3>
                <p className="text-sm text-gray-600">Programs & Curriculum</p>
              </div>
              <div onClick={() => handleQuickInfoClick("I need support")} className="bg-white/70 dark:bg-gray-900/70 backdrop-blur-sm p-6 rounded-xl border border-gray-200 dark:border-gray-800 hover:shadow-lg transition-shadow duration-200 cursor-pointer">
                <div className="bg-gradient-to-br from-orange-100 to-orange-200 p-3 rounded-lg w-fit mb-4">
                  <Phone className="h-6 w-6 text-brand" />
                </div>
                <h3 className="font-semibold text-gray-900 mb-2">Support</h3>
                <p className="text-sm text-gray-600">24/7 Help Available</p>
              </div>
              <div onClick={() => handleQuickInfoClick("Can we chat?")} className="bg-white/70 dark:bg-gray-900/70 backdrop-blur-sm p-6 rounded-xl border border-gray-200 dark:border-gray-800 hover:shadow-lg transition-shadow duration-200 cursor-pointer">
                <div className="bg-gradient-to-br from-orange-100 to-orange-200 p-3 rounded-lg w-fit mb-4">
                  <MessageCircle className="h-6 w-6 text-brand" />
                </div>
                <h3 className="font-semibold text-gray-900 mb-2">Chat</h3>
                <p className="text-sm text-gray-600">Instant Responses</p>
              </div>
            </div>

      {/* Footer */}
      <div className="mt-8 text-center text-sm text-gray-500">
        <p>RGM College of Engineering and Technology - Established 1995 | Top 100 Universities | 15,000+ Students</p>
      </div>
    </div>
  );
}

export default App;