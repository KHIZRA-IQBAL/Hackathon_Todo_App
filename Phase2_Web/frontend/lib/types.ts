export interface User {
    id: number;
    email: string;
    full_name?: string;
  }
  
  export interface Task {
    id: number;
    title: string;
    description: string;
    completed: boolean;
    created_at: string;
    updated_at: string;
  }
  