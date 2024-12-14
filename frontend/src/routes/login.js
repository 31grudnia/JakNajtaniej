import { VStack, Input, Button } from "@chakra-ui/react"
import { Field } from "../components/ui/field"
import { PasswordInput } from "../components/ui/password-input"
import { useState } from "react"

import { login } from "../endpoints/api"


const Login = () => {

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const handleLogin = () => {
        login(username, password)
    }

    return (
     
        <VStack>
            <Field label="Username" required errorText="This field is required">
                <Input placeholder="Enter your username" onChange={(e) => setUsername(e.target.value)} value={username} />
            </Field>
            <Field label="Password" required errorText="This field is required">
                <PasswordInput placeholder="Enter your password" onChange={(e) => setPassword(e.target.value)} value={password} />
            </Field>
            <Button variant="surface" onClick={handleLogin}>Login</Button>
        </VStack>
    )
}

export default Login;